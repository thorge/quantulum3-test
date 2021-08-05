from quantulum3 import parser
import json


def test(input):
    values = 0
    entities = 0
    units = 0

    i = 0
    for testCase in input:
        try:
            quants = parser.parse(testCase['text'])
            print(f'({i}): ' + testCase['text'])
            print(quants)
            i += 1
            if quants[0].unit.name == testCase['unit']:
                units += 1
            if quants[0].unit.entity.name == testCase['entity']:
                entities += 1
            if quants[0].value == float(testCase['value']):
                values += 1
        except:
            print('Could not process testcase: ' + testCase['text'])

    result = {
        "total": len(input),
        "evaluation": {
            "values": values,
            "entities": entities,
            "units": units
        }
    }

    return result


### Testing ###
res = {}

# Test Mass Accumulation Rates
print("### Testing mass accumulation rates: ###\n")
with open("test-mar.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
res['mass accumulation rates'] = test(jsonObject['data'])


# Test Sedimentation Rates
print("\n\n### Testing sedimentation rates: ###\n")
with open("test-sr.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
res['sedimentation rates'] = test(jsonObject['data'])

# Print results
print('\n### RESULT ###')
print(res)
