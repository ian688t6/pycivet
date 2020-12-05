from regmap import RegMap

if __name__ == '__main__':
    rmap = RegMap()
    rmap.load('CWQ2100R0_RegisterMap_draft_v0.0.8_cal_v1.1.xlsx')
    print(rmap.get_regblocks())
    regmaplist = rmap.get_regmap('EXT_REG')
    for regdata in regmaplist:
        print(regdata)