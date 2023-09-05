class Templates():

    def __init__(self,spec):
        self.spec = spec

    @property
    def outOfRangeHex(self):
        return "the response is not within the acceptable hex range."

    @property
    def statusCode(self):
        return "does not reflect an ECU in application or bootloader mode."


class Uds2Templates(Templates):

    def __init__(self,spec='UDS+2'):
        super().__init__(spec)

    @property
    def invalidPartNumber(self):
        return "According to CS.00102, In application and bootloader modes the ECU is returning an invalid 'EBOM ECU Part Number'. The ECU shall return a \"EBOM ECU Part Number\" with valid ASCII characters  – 8 numeric followed by 2 alpha with a range of 0x30 - 0x39, 0x41 - 0x5A (e.g: 12345678AA)"

    @property
    def onlySupportsOnePartNumber(self):
        return "If the ECU supports only one ECU Part Number (either 0xF132 or 0xF187), the unused DID shall be supported and filled with 0x20 ASCII white space characters. If the ECU is not assigned or uses CoDep part number ($F132).  The ECU shall report the identical information regardless of the current mode (application software or bootloader) in all available sessions."

    @property
    def appAndBootMode(self):
        return "In application and bootloader modes, the responses are not identical.  According to CS.00102, The ECU shall report the identical information regardless of the current mode (application software or bootloader) in all available sessions"

    def appInvalidRanges(self,bytes,did=''):
        t = []
        if did == 'F1 81':
            for k, v in bytes.items():
                # Byte 3 (# of LBs)
                if k == 3:
                    t.append(f'{v}')
                # Byte 4 (SW - Year)
                elif k in [4,17,30,43,56,69,82,95,108,121,134,147,160,173,186,199,212,225,238,251,264,277,290,303,316,329,342,355,368,381,394,407,420,433,446,459,472,485,498,511,524,537,550,563,576,589,602,615,628,641,654,667,680,693,706,719,732,745,758,771,784,797,810,823,836,849,862,875,888,901,914,927,940,953,966,979,992,1005,1018,1031,1044,1057,1070,1083,1096,1109,1122,1135,1148,1161,1174,1187,1200,1213,1226,1239,1252,1265,1278,1291]:
                    t.append(f'Byte {k} (SW Year) - {v} is not within the acceptable range defined in CS.00102 (0x00 - 0x63)')
                # Byte 5 (SW Week)
                elif k in [5,18,31,44,57,70,83,96,109,122,135,148,161,174,187,200,213,226,239,252,265,278,291,304,317,330,343,356,369,382,395,408,421,434,447,460,473,486,499,512,525,538,551,564,577,590,603,616,629,642,655,668,681,694,707,720,733,746,759,772,785,798,811,824,837,850,863,876,889,902,915,928,941,954,967,980,993,1006,1019,1032,1045,1058,1071,1084,1097,1110,1123,1136,1149,1162,1175,1188,1201,1214,1227,1240,1253,1266,1279,1292]:
                    t.append(f'Byte {k} (SW Week) - {v} is not within the acceptable range defined in CS.00102 (0x01 - 0x34)')
                elif k == 'NUMBER OF LBs':
                    t.append(f'Byte 3 - {v}')
                else:
                    t.append(f'Byte {k} - {v} is not within the acceptable range defined in CS.00102 (20;30-39;41-5A)')
            #return f'In application mode, the following bytes are returning invalid/out-of-range data.  {t}'
            mess1 = 'In application mode, the following bytes are returning invalid/out-of-range data.'
            for x in t:
                temp = mess1
                temp = temp + ' ' + x
                mess1 = temp
            return mess1
        elif did == 'F1 80':
            for k, v in bytes.items():
                # Byte 3 (# of LBs)
                if k == '3':
                    t.append(f'{v}')
                # Byte 4 (SW - Year)
                elif k in [4,17,30,43,56,69,82,95,108,121,134,147,160,173,186,199,212,225,238,251,264,277,290,303,316,329,342,355,368,381,394,407,420,433,446,459,472,485,498,511,524,537,550,563,576,589,602,615,628,641,654,667,680,693,706,719,732,745,758,771,784,797,810,823,836,849,862,875,888,901,914,927,940,953,966,979,992,1005,1018,1031,1044,1057,1070,1083,1096,1109,1122,1135,1148,1161,1174,1187,1200,1213,1226,1239,1252,1265,1278,1291]:
                    t.append(f'Byte {k} (SW Year) - {v} is not within the acceptable range defined in CS.00102 (0x00 - 0x63)')
                # Byte 5 (SW Week)
                elif k in [5,18,31,44,57,70,83,96,109,122,135,148,161,174,187,200,213,226,239,252,265,278,291,304,317,330,343,356,369,382,395,408,421,434,447,460,473,486,499,512,525,538,551,564,577,590,603,616,629,642,655,668,681,694,707,720,733,746,759,772,785,798,811,824,837,850,863,876,889,902,915,928,941,954,967,980,993,1006,1019,1032,1045,1058,1071,1084,1097,1110,1123,1136,1149,1162,1175,1188,1201,1214,1227,1240,1253,1266,1279,1292]:
                    t.append(f'Byte {k} (SW Week) - {v} is not within the acceptable range defined in CS.00102 (0x01 - 0x34)')
                elif k == 'NUMBER OF LBs':
                    t.append(f'byte 3 - {v}')
                else:
                    t.append(f'Byte {k} - {v} is not within the acceptable range defined in CS.00102 (20;30-39;41-5A)')
            #return f'In application mode, the following bytes are returning invalid/out-of-range data.  {t}'
            mess1 = 'In application mode, the following bytes are returning invalid/out-of-range data.'
            for x in t:
                temp = mess1
                temp = temp + ' ' +  x
                mess1 = temp

            return mess1
        elif did == 'F1 82':
            for k, v in bytes.items():
                # Byte 3 (# of LBs)
                if k == '3':
                    t.append(f'{v}')
                # Byte 4 (SW - Year)
                elif k in [4,17,30,43,56,69,82,95,108,121,134,147,160,173,186,199,212,225,238,251,264,277,290,303,316,329,342,355,368,381,394,407,420,433,446,459,472,485,498,511,524,537,550,563,576,589,602,615,628,641,654,667,680,693,706,719,732,745,758,771,784,797,810,823,836,849,862,875,888,901,914,927,940,953,966,979,992,1005,1018,1031,1044,1057,1070,1083,1096,1109,1122,1135,1148,1161,1174,1187,1200,1213,1226,1239,1252,1265,1278,1291]:
                    t.append(f'Byte {k} (SW Year) - {v} is not within the acceptable range defined in CS.00102 (0x00 - 0x63)')
                # Byte 5 (SW Week)
                elif k in [5,18,31,44,57,70,83,96,109,122,135,148,161,174,187,200,213,226,239,252,265,278,291,304,317,330,343,356,369,382,395,408,421,434,447,460,473,486,499,512,525,538,551,564,577,590,603,616,629,642,655,668,681,694,707,720,733,746,759,772,785,798,811,824,837,850,863,876,889,902,915,928,941,954,967,980,993,1006,1019,1032,1045,1058,1071,1084,1097,1110,1123,1136,1149,1162,1175,1188,1201,1214,1227,1240,1253,1266,1279,1292]:
                    t.append(f'Byte {k} (SW Week) - {v} is not within the acceptable range defined in CS.00102 (0x01 - 0x34)')
                elif k == 'NUMBER OF LBs':
                    t.append(f'byte 3 - {v}')
                else:
                    t.append(f'Byte {k} - {v} is not within the acceptable range defined in CS.00102 (20;30-39;41-5A)')
            #return f'In application mode, the following bytes are returning invalid/out-of-range data.  {t}'
            mess1 = 'In application mode, the following bytes are returning invalid/out-of-range data.'
            for x in t:
                temp = mess1
                temp = temp + ' ' + x
                mess1 = temp

            return mess1
        elif did == '20 10':
            for k, v in bytes.items():
                if k == 3 and v != 'FF':
                # t.append(f'byte {k} - {v} does not reflect an ECU in application mode.  Please see CS.00102 for more information.')
                    t.append(f'Byte {k} - {v} does not reflect an ECU in application mode.  Please see CS.00102 for more information.')
                elif k == 4 and v != '00':
                    t.append(f'Byte {k} is not within the value of an ECU in application mode ({v}).  According to CS.00102, this byte should return 0x00 for an ECU in application mode.')
        else:
            for k, v in bytes.items():
                t.append(f'Byte {k} - {v} is not within the acceptable range defined in CS.00102 (20;30-39;41-5A)')
            #return f'In application mode, the following bytes are returning invalid/out-of-range data.  {t}.'
            mess1 = 'In application mode, the following bytes are returning invalid/out-of-range data.'
            for x in t:
                temp = mess1
                temp = temp + ' ' + x
                mess1 = temp

            return mess1

    def bootInvalidRanges(self,bytes,did=''):
        t = []
        if did == 'F1 80':
            for k, v in bytes.items():
                # Byte 3 (# of LBs)
                if k == 3:
                    t.append(f'{v}')
                # Byte 4 (SW - Year)
                elif k in [4,17,30,43,56,69,82,95,108,121,134,147,160,173,186,199,212,225,238,251,264,277,290,303,316,329,342,355,368,381,394,407,420,433,446,459,472,485,498,511,524,537,550,563,576,589,602,615,628,641,654,667,680,693,706,719,732,745,758,771,784,797,810,823,836,849,862,875,888,901,914,927,940,953,966,979,992,1005,1018,1031,1044,1057,1070,1083,1096,1109,1122,1135,1148,1161,1174,1187,1200,1213,1226,1239,1252,1265,1278,1291]:
                    t.append(f'Byte {k} (SW Year) - {v} is not within the acceptable range defined in CS.00102 (0x00 - 0x63)')
                # Byte 5 (SW Week)
                elif k in [5,18,31,44,57,70,83,96,109,122,135,148,161,174,187,200,213,226,239,252,265,278,291,304,317,330,343,356,369,382,395,408,421,434,447,460,473,486,499,512,525,538,551,564,577,590,603,616,629,642,655,668,681,694,707,720,733,746,759,772,785,798,811,824,837,850,863,876,889,902,915,928,941,954,967,980,993,1006,1019,1032,1045,1058,1071,1084,1097,1110,1123,1136,1149,1162,1175,1188,1201,1214,1227,1240,1253,1266,1279,1292]:
                    t.append(f'Byte {k} (SW Week) - {v} is not within the acceptable range defined in CS.00102 (0x01 - 0x34)')
                elif k == 'NUMBER OF LBs':
                    t.append(f'Byte 3 - {v}')
                else:
                    t.append(f'Byte {k} - {v} is not within the acceptable range defined in CS.00102 (20;30-39;41-5A)')
            #return f'In Bootloader mode, the following bytes are returning invalid/out-of-range data.  {t}'
            mess1 = 'In Bootloader mode, the following bytes are returning invalid/out-of-range data.'
            for x in t:
                temp = mess1
                temp = temp + ' ' + x
                mess1 = temp

            return mess1

        elif did == '20 10':
            for k,v in bytes.items():
                print(type(k))
                if k == 3:
                    t.append(f'Byte {k} is not reflecting an ECU in bootloader mode ({v}).  According to CS.00102, the lowest value for byte 3 for an ECU in bootloader mode is 0x80.  Please review CS.00102 for more information.')
                elif k == 4:
                    t.append(f'Byte {k} is out-of-range of what is defined in CS.00102 ({v}).  According to CS.00102, the defined ranges are (00 - 05).')
                else:
                    pass
                #return f'In bootloader mode, the following bytes are returning invalid/out-of-range data. {t}'
                mess1 = 'In Bootloader mode, the following bytes are returning invalid/out-of-range data.'
                for x in t:
                    temp = mess1
                    temp = temp + ' ' + x
                    mess1 = temp
                return mess1
        else:
            for k,v in bytes.items():
                t.append(f'Byte {k} - {v}')
            #return f'In bootloader mode, the following bytes are returning invalid/out-of-range data. {t}.  According to CS.00102, the acceptable hex range is defined as (20; 30-39; 41-5A)'
            for x in t:
                temp = mess1
                temp = temp  + ' ' + x
                mess1 = temp
            return mess1


    def appAndBootInvalidRanges(self,app,boot):
        return f"In application and bootloader mode, the following bytes are returning invalid/out-of-range data.  App mode {app}.  Boot mode {boot}"

    @property
    def expectedResponse(self):
        return f'This DID is optional, but if supported it is expected that the module report identical  information  regardless  of  the current mode (application software or bootloader) in all available sessions.'
