cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

project(c_mat_mul)

# you can set variables
set(RPATH "")
set(CMAKE_SKIP_BUILD_RPATH TRUE)

if (${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_CURRENT_LIST_DIR})
    if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
        set(CMAKE_BUILD_TYPE Release CACHE STRING "" FORCE)
    endif()
endif()

# set source and header
file(GLOB C_MAT_MUL_SOURCE ${CMAKE_CURRENT_LIST_DIR}/src/*.c)
file(GLOB C_MAT_MUL_HEADER ${CMAKE_CURRENT_LIST_DIR}/include/*.h)

# # -------- here we build an executable --------- #
# add_executable(c_mat_mul ${C_MAT_MUL_SOURCE} ${C_MAT_MUL_HEADER})

# # ---------- here we build a static library ------ # can be used for other project to link
# add_library(
#     c_mat_mul STATIC
#     ${C_MAT_MUL_SOURCE}
#     ${C_MAT_MUL_HEADER}
# )

# ---------- here we build a dynamic library ------ # 
add_library(
    c_mat_mul SHARED
    ${C_MAT_MUL_SOURCE}
    ${C_MAT_MUL_HEADER}
)


# -------------- include some paths ------------- #
target_include_directories(c_mat_mul PUBLIC "./")
target_include_directories(c_mat_mul PRIVATE ${CMAKE_CURRENT_LIST_DIR}/include)


# ---------- if other library is neede, you can link other libraries ------- #
# target_link_libraries(c_mat_mul liba libb)