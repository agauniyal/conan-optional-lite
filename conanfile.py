from conans import ConanFile, tools

class OptionalliteConan(ConanFile):
    name = "optional-lite"
    version = "2.2.0"
    license = "MIT"
    url = "https://github.com/martinmoene/optional-lite"
    description = "A single-file header-only version of a C++17-like optional, a nullable object for C++98, C++11 and later"

    def source(self):
        self.run("git clone https://github.com/martinmoene/optional-lite.git")
        self.run("cd optional-lite && git checkout v2.2.0")

    def package(self):
        self.copy(pattern="*.hpp", src="optional-lite/include/nonstd", dst="include", keep_path=False)
