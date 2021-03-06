"""Test for wsdottraffic.armcalc.ArmCalcClient
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import unittest
from datetime import date
from armcalcsvc import (
    ArmCalcInput, ArmCalcOutput, ArmCalcClient)


class TestArmCalc(unittest.TestCase):
    """Defines a unit test case for testing armcalcclient
    """

    def test_batch(self):
        """Test batch conversion
        """
        the_date = date(2014, 8, 19)

        input_list = [
            {"CalcType": 1, "SR": "005", "ReferenceDate": the_date,
             "ARM": 0.32, "ResponseDate": the_date},
            {"CalcType": 0, "SR": "005", "ReferenceDate": the_date,
             "SRMP": 150.0, "ResponseDate": the_date}
        ]
        data = []
        for item in input_list:
            aci = ArmCalcInput(**item)
            data.append(aci)
        client = ArmCalcClient()
        result = client.batch(data)

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, ArmCalcOutput)
            if item.CalculationReturnCode == 0:
                map(self.assertIsNotNone, (item.SR, item.ARM, item.SRMP))

    def test_route_id_property(self):
        """Tests the RouteID property
        """
        aci = ArmCalcInput()
        aci.RouteID = "002COABERDN"
        self.assertEqual(aci.SR, "002")
        self.assertEqual(aci.RRT, "CO")
        self.assertEqual(aci.RRQ, "ABERDN")

        self.assertEqual(aci.RouteID, aci.SR + aci.RRT + aci.RRQ)

        aci.RouteID = "5"
        self.assertEqual(aci.SR, "005")


if __name__ == "__main__":
    unittest.main()
