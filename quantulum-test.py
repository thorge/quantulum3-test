from quantulum3 import parser
import json


def test(input):
    values = 0
    entities = 0
    units = 0
    total = 0

    i = 0
    for testCase in input:
        try:
            quants = parser.parse(testCase['text'])
            print(f'({i}): ' + testCase['text'])
            print(quants)
            i += 1
            for measurement in testCase['measurements']:
                total += 1
                key = 0
                for quant in quants:
                    if quant.unit.name == measurement['unit']:
                        units += 1
                        print("Unit matches.")
                    if quant.unit.entity.name == measurement['entity']:
                        entities += 1
                        print("Entity matches.")
                    if quant.value == float(measurement['value']):
                        values += 1
                        print("Value matches.")
            print("\n")
        except:
            print('Could not process testcase: ' + testCase['text'])

    result = {
        "total": total,
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
print(json.dumps(res, indent=4, sort_keys=False))
