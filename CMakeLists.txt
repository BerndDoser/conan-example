cmake_minimum_required(VERSION 3.0)
project(cmake_example VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# # Conan
# find_program(CONAN conan)
# if(CONAN)
#     if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
#        message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
#        file(DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/v0.14/conan.cmake"
#                      "${CMAKE_BINARY_DIR}/conan.cmake")
#     endif()
    
#     # Conan setup
#     include(${CMAKE_BINARY_DIR}/conan.cmake)
#     conan_cmake_run(CONANFILE conanfile.py
#                     BASIC_SETUP CMAKE_TARGETS NO_OUTPUT_DIRS
#                     SETTINGS compiler.libcxx=libstdc++11
#                     BUILD_TYPE "None"
#                     BUILD missing)
    
#     include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#     set(CONAN_SYSTEM_INCLUDES "On")
#     conan_basic_setup()
# endif()

add_subdirectory(src)
