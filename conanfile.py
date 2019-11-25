from conans import ConanFile, CMake

class ConanExampleConan(ConanFile):
    
    name = "conan_example"
    version = "1.0"
    license = "MIT"
    description = "C++ example using CMake and conan.io"
    homepage = "https://github.com/BerndDoser/conan_example"
    url = "https://github.com/BerndDoser/conan_example.git"
    
    exports_sources = "include/*", "test/*", "CMakeLists.txt"
    no_copy_source = True
    
    settings = "os", "compiler", "build_type", "arch"
    requires = \
        "gtest/1.8.1@bincrafters/stable", \
        "pybind11/2.3.0@conan/stable"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.so", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")

    def package_id(self):
        self.info.header_only()
