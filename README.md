# FILD

FILD is a library for contract testing. FILD allows to store descriptive 
structure of the API and use it further for generating test data based on Faker.

The basic type for usage is Fild, any other types should inherit from.
Field supports the description of the API parameter within the following:\
`name`: key in json\
`required`: identifies the necessity of presense of the 
key in the resulting json.\
`allow_none`: should be true if the value can be null in the
json.\
`default`: default value to be used in regular generation.
Can either be the value or the callable to generate.

Abstract method `generate_value` is used to specify the rules
based on which the value should be generated. When defining
new type, inherited from Field, the method should be overriden
to describe the generation procedure.

Library supports multi-level hierarchy with Arrays and Dictionaries.

Library also provides some dict operating methods.\
`filter_dict`: allows to apply value/callable filter to dict by values\
`merge_with_updates`: merges two dicts with either overriding or only adding
values to the target dictionary.\
`normalize`: sorts lists - both top level and embeded - to represent
the desired order.
