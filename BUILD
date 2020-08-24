py_library(
    name = "variable",
    srcs = ["variable.py"],
)

py_test(
    name = "test",
    srcs = ["test.py"],
    deps = [":variable"],
)

py_library(
    name = "geometry",
    srcs = ["geometry.py"],
    deps = [":variable"],
)

py_binary(
    name = "model",
    srcs = ["model.py"],
    deps = [
        ":geometry",
        ":variable",
    ],
)
