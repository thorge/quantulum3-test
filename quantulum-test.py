from quantulum3 import parser
import json

#from quantulum3.load import add_custom_unit, remove_custom_unit


#add_custom_unit(name="schlurp", surfaces=["slp"], entity="dimensionless")
#parser.parse("This extremely sharp tool is precise up to 0.5 slp")


def test(input):
    i = 1
    for testCase in input:
        print(f'({i}): ' + testCase['text'])
        quants = parser.parse(testCase['text'])
        print(quants)
        print('\n')
        i += 1


# Test Mass Accumulation Rates
print("### Testing mass accumulation rates: ###\n")
with open("test-mar.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
test(jsonObject['input'])


# Test Sedimentation Rates
print("\n\n### Testing sedimentation rates: ###\n")
with open("test-sr.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
test(jsonObject['input'])
