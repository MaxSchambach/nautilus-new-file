cmake_minimum_required(VERSION 2.6)
project(NautilusLatex NONE)

set (NautilusNewFile_VERSION_MAJOR 1)
set (NautilusNewFile_VERSION_MINOR 0)

# Configurable paths
set(EXT_PATH "~/.local/share/nautilus-python/extensions" CACHE FILEPATH "Path to Nautilus extension.")

# Configure files
configure_file(nautilus-new-file.py nautilus-new-file.py)

# Extensions files
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/nautilus-new-file.py"
        PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ GROUP_EXECUTE GROUP_READ WORLD_EXECUTE WORLD_READ
        DESTINATION ${EXT_PATH})

# Uninstall target
configure_file("${CMAKE_CURRENT_SOURCE_DIR}/cmake/cmake_uninstall.cmake.in"
               "${CMAKE_CURRENT_BINARY_DIR}/cmake/cmake_uninstall.cmake" IMMEDIATE @ONLY)
add_custom_target(uninstall COMMAND ${CMAKE_COMMAND}
                  -P ${CMAKE_CURRENT_BINARY_DIR}/cmake/cmake_uninstall.cmake)
