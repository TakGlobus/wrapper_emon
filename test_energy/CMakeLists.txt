cmake_minimum_required(VERSION 3.10)

find_package(PkgConfig REQUIRED)
pkg_check_modules(ENERGYMON REQUIRED energymon-osp)
include_directories(${ENERGYMON_INCLUDE_DIRS})

#find_package(PkgConfig REQUIRED)
#pkg_check_modules(ENERGYMON REQUIRED energymon-osp-polling)
#include_directories(${ENERGYMON_INCLUDE_DIRS})

add_executable(em em.c)
target_link_libraries(em -L${ENERGYMON_LIBDIR} ${ENERGYMON_LIBRARIES} -L/usr/local/lib -lenergymon-osp -lhidapi-libusb  )
#target_link_libraries(em -L${ENERGYMON_LIBDIR} ${ENERGYMON_LIBRARIES} -L/usr/local/lib -lenergymon-osp -lhidapi-libusb  -L/usr/local/lib -lenergymon-osp-polling -lpthread -lhidapi-libusb )
