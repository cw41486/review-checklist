class Specification():

    def __init__(self, spec):
        self.spec = spec

    def getFullHexRange(self):
        fullRange = []

        for x in range(int('0x00', 16), int('0xFF',16) + 1):
            fullRange.append(x)

        for x in range(len(fullRange)):
            # fullRange[x] = str(hex(fullRange[x]))
            fullRange[x] = format(fullRange[x],'02x')

        for x in range(len(fullRange)):
            fullRange[x] = fullRange[x].lower()

        return fullRange

    def getValidInputRange(self,start,end):
        validRange = []
        for x in range(int(start, 16), int(end,16) + 1):
            validRange.append(x)

        for x in range(len(validRange)):
            # validRange[x] = str(hex(validRange[x]))[2:]
            validRange[x] = format(validRange[x],'02x')

        for x in range(len(validRange)):
            validRange[x] = validRange[x].lower()

        return validRange



    def getValidAsciiRange(self):
        validRange = []

        validRange.append(int('0x2D', 16))
        validRange.append(int('0x20',16))

        for x in range(int('0x30', 16), int('0x39', 16) + 1):
            validRange.append(x)

        for x in range(int('0x41', 16), int('0x5A', 16) + 1):
            validRange.append(x)

        for x in range(len(validRange)):
            # validRange[x] = str(hex(validRange[x]))[2:]
            validRange[x] = format(validRange[x],'02x')

        for x in range(len(validRange)):
            validRange[x] = validRange[x].lower()

        return validRange


class Cusw(Specification):
    def __init__(self,spec='CUSW'):
        super().__init__(spec)

    @property
    def dids(self):
        protocol_dids = {'F1 00':self.getFullHexRange(),
                         'F1 0D':self.getFullHexRange(),
                         'F1 32': {
                                3:self.getValidInputRange('0x30','0x39'),
                             4:self.getValidInputRange('0x30','0x39'),
                             5:self.getValidInputRange('0x30','0x39'),
                             6:self.getValidInputRange('0x30','0x39'),
                             7:self.getValidInputRange('0x30','0x39'),
                             8:self.getValidInputRange('0x30','0x39'),
                             9:self.getValidInputRange('0x30','0x39'),
                             10:self.getValidInputRange('0x30','0x39'),
                             11:self.getValidInputRange('0x41','0x5A'),
                             12:self.getValidInputRange('0x41','0x5A')
                         },
                         'F1 22':self.getValidAsciiRange(),
                         'F1 12':self.getValidAsciiRange(),
                         'F1 58':self.getFullHexRange(),
                         'F1 80':self.getFullHexRange(),
                         'F1 81':self.getFullHexRange(),
                         'F1 82':self.getFullHexRange(),
                         'F1 92':self.getFullHexRange(),
                         'F1 93':self.getFullHexRange(),
                         'F1 94':self.getFullHexRange(),
                         'F1 95':self.getFullHexRange()
        }

class Uds(Specification):

    def __init__(self,spec='UDS'):
        super().__init__(spec)

    @property
    def dids (self):
        protocol_dids = {'01 00':self.getFullHexRange(),
                         #'F1 0D':self.getFullHexRange(),
                         'F1 0D':{3:self.getValidInputRange('0x00','0x0C'),
                                  4:self.getValidInputRange('0x67','0x6C'),
                                  5:self.getValidInputRange('0xB8','0xBD'),
                                  6:self.getValidInputRange('0xD0','0xD4')
                         },
                         'F1 00':self.getFullHexRange(),
                         'F1 12':self.getValidAsciiRange(),
                         'F1 22':self.getValidAsciiRange(),
                         'F1 32': {
                                3:self.getValidInputRange('0x30','0x39'),
                             4:self.getValidInputRange('0x30','0x39'),
                             5:self.getValidInputRange('0x30','0x39'),
                             6:self.getValidInputRange('0x30','0x39'),
                             7:self.getValidInputRange('0x30','0x39'),
                             8:self.getValidInputRange('0x30','0x39'),
                             9:self.getValidInputRange('0x30','0x39'),
                             10:self.getValidInputRange('0x30','0x39'),
                             11:self.getValidInputRange('0x41','0x5A'),
                             12:self.getValidInputRange('0x41','0x5A')
                         },
                         'F1 51':self.getFullHexRange(),
                         'F1 53':self.getFullHexRange(),
                         'F1 54':self.getFullHexRange(),
                         'F1 55':self.getFullHexRange(),
                         'F1 58':self.getFullHexRange()}
        return protocol_dids


class Fiat(Specification):      #   See latest revision of CS.00021 Rev F. (as of 21-Dec-2022)

    def __init__(self, spec='Fiat'):
        super().__init__(spec)

    @property
    def dids(self):
        protocol_dids = {
                    'F1 0D':{3:self.getValidInputRange('0x80','0x8B'),
                             4:self.getValidInputRange('0x80','0x8B'),
                             5:self.getValidInputRange('0xFF','0xFF'),  # Byte not supported, should always be 0xFF.
                             6:self.getValidInputRange('0x80','0x8A'),
                             7:self.getValidInputRange('0x80','0x89')
                    },
                    'F1 92':self.getFullHexRange(),
                    'F1 93':self.getFullHexRange(),
                    'F1 94':self.getFullHexRange(),
                    'F1 95':self.getFullHexRange(),
                    'F1 32': {
                            3:self.getValidInputRange('0x30','0x39'),
                             4:self.getValidInputRange('0x30','0x39'),
                             5:self.getValidInputRange('0x30','0x39'),
                             6:self.getValidInputRange('0x30','0x39'),
                             7:self.getValidInputRange('0x30','0x39'),
                             8:self.getValidInputRange('0x30','0x39'),
                             9:self.getValidInputRange('0x30','0x39'),
                             10:self.getValidInputRange('0x30','0x39'),
                             11:self.getValidInputRange('0x41','0x5A'),
                             12:self.getValidInputRange('0x41','0x5A')
                         },
                    'F1 22':self.getValidAsciiRange(),
                    'F1 12':self.getValidAsciiRange(),
                    'F1 00':self.getFullHexRange(),
                    'F1 80':self.getFullHexRange(),
                    'F1 81':self.getFullHexRange(),
                    'F1 82':self.getFullHexRange(),
                    'F1 A0':self.getFullHexRange(),
                    '20 10':self.getFullHexRange()

        }
        return protocol_dids


class UDS_2(Specification):     # Latest revision CS.00102 Rev E.  Oct,2020

    def __init__(self,spec='UDS+2'):
        super().__init__(spec)

    @property
    def mandatoryDids(self):
        dids = [
            'F1 10',
            'F1 32',
            'F1 80',
            'F1 88',
            'F1 91',
            'F1 92',
            'F1 93',
            'F1 94',
            'F1 95',
            'F1 87',
            'F1 8A',
            'F1 8B'
        ]
        return dids


    @property
    def dids(self):

        protocol_dids = {
                        #'20 10':self.getFullHexRange(),
                        '20 10': {
                                  3: self.getValidInputRange('0x80','0xFF'),
                                  4: self.getValidInputRange('0x00','0x05')
                                  },
                        'F1 0D': {3: self.getValidInputRange('0x90', '0x95'),
                                  4: self.getValidInputRange('0x30', '0x36'),
                                  5: self.getValidInputRange('0x40', '0xFF'),
                                  6: self.getValidInputRange('0x50', '0x57')
                                  },
                        'F1 10':{ 3:self.getFullHexRange(),
                                  4:self.getValidInputRange('0x00','0xFE'),
                                  5:self.getFullHexRange(),
                                  6:self.getFullHexRange(),
                                  7:self.getFullHexRange(),
                                  8:self.getFullHexRange(),
                                  9:self.getFullHexRange(),
                                  10:self.getFullHexRange(),
                                  11:self.getFullHexRange(),
                                  12:self.getFullHexRange()
                                  },
                         'F1 12':self.getValidAsciiRange(),
                         'F1 22':self.getValidAsciiRange(),
                         'F1 32': {
                                3:self.getValidInputRange('0x30','0x39'),
                             4:self.getValidInputRange('0x30','0x39'),
                             5:self.getValidInputRange('0x30','0x39'),
                             6:self.getValidInputRange('0x30','0x39'),
                             7:self.getValidInputRange('0x30','0x39'),
                             8:self.getValidInputRange('0x30','0x39'),
                             9:self.getValidInputRange('0x30','0x39'),
                             10:self.getValidInputRange('0x30','0x39'),
                             11:self.getValidInputRange('0x41','0x5A'),
                             12:self.getValidInputRange('0x41','0x5A')
                         },
                         'F1 87':self.getValidAsciiRange(),
                         'F1 54':self.getFullHexRange(),
                         'F1 55':self.getFullHexRange(),
                         'F1 58':self.getValidAsciiRange(),
                         'F1 8A':self.getValidAsciiRange(),
                         'F1 8B':self.getValidAsciiRange(),
                         'F1 81':{3:self.getValidInputRange('0x01','0xFF'),
                                  4:self.getValidInputRange('0x00','0x63'),
                                  5:self.getValidInputRange('0x01','0x34'),
                                  6:self.getFullHexRange(),
                                  7: self.getValidAsciiRange(),
                                  8: self.getValidAsciiRange(),
                                  9: self.getValidAsciiRange(),
                                  10: self.getValidAsciiRange(),
                                  11: self.getValidAsciiRange(),
                                  12: self.getValidAsciiRange(),
                                  13: self.getValidAsciiRange(),
                                  14: self.getValidAsciiRange(),
                                  15: self.getValidAsciiRange(),
                                  16: self.getValidAsciiRange()
                                  },
                        'F1 80': {3: self.getValidInputRange('0x01', '0xFF'),
                                  4: self.getValidInputRange('0x00', '0x63'),
                                  5: self.getValidInputRange('0x01', '0x34'),
                                  6: self.getFullHexRange(),
                                  7: self.getValidAsciiRange(),
                                  8: self.getValidAsciiRange(),
                                  9: self.getValidAsciiRange(),
                                  10: self.getValidAsciiRange(),
                                  11: self.getValidAsciiRange(),
                                  12: self.getValidAsciiRange(),
                                  13: self.getValidAsciiRange(),
                                  14: self.getValidAsciiRange(),
                                  15: self.getValidAsciiRange(),
                                  16: self.getValidAsciiRange()
                                  },
                         'F1 82':{3:self.getValidInputRange('0x01','0xFF'),
                                  4: self.getValidInputRange('0x00', '0x63'),
                                  5: self.getValidInputRange('0x01', '0x34'),
                                  6: self.getFullHexRange(),
                                  7: self.getValidAsciiRange(),
                                  8: self.getValidAsciiRange(),
                                  9: self.getValidAsciiRange(),
                                  10: self.getValidAsciiRange(),
                                  11: self.getValidAsciiRange(),
                                  12: self.getValidAsciiRange(),
                                  13: self.getValidAsciiRange(),
                                  14: self.getValidAsciiRange(),
                                  15: self.getValidAsciiRange(),
                                  16: self.getValidAsciiRange()
                                  },
                         'F1 88':self.getValidAsciiRange(),
                         'F1 91':self.getValidAsciiRange(),
                         'F1 92':self.getValidAsciiRange(),
                         'F1 93':self.getFullHexRange(),
                         'F1 94':self.getValidAsciiRange(),
                         'F1 95':self.getFullHexRange(),
                         'F1 8C': { 3: ['54'],
                                    4: self.getFullHexRange(),
                                    5: self.getValidAsciiRange(),
                                    6: self.getValidAsciiRange(),
                                    7: self.getValidAsciiRange(),
                                    8: self.getValidAsciiRange(),
                                    9: self.getValidAsciiRange(),
                                    10: self.getValidAsciiRange(),
                                      11: self.getValidAsciiRange(),
                                      12: self.getValidAsciiRange(),
                                      13: self.getValidAsciiRange(),
                                      14: self.getValidAsciiRange(),
                                      15: self.getValidAsciiRange(),
                                      16: self.getValidAsciiRange(),
                                      17: self.getValidAsciiRange()
                      }
                         }


        return protocol_dids





