cmake_minimum_required(VERSION 3.10)

find_package(PkgConfig REQUIRED)
pkg_check_modules(ENERGYMON REQUIRED energymon-osp)
include_directories(${ENERGYMON_INCLUDE_DIRS})


add_executable(testem test4.c)
target_link_libraries(testem -L${ENERGYMON_LIBDIR} ${ENERGYMON_LIBRARIES} -L/usr/local/lib -lenergymon-osp -lhidapi-libusb  )
