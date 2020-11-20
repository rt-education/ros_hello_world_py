cmake_minimum_required(VERSION 3.0.2)
project(hello_world_py)

# 必要なパッケージを探す
# Finding the required packages
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

# catkin packageを宣言
# Declaring the catkin package
catkin_package(
  CATKIN_DEPENDS rospy std_msgs
)

# ヘッダーファイルの場所を定義
# Configuring the destination of the header files
include_directories(
  include ${catkin_INCLUDE_DIRS}
)

# 便利な関数を宣言
# Convenient function
function(custom_install target)
  catkin_install_python(PROGRAMS scripts/${target}.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION} )
endfunction()

# talkerとlistenerに必要なものをインストールさせる
# Installs the needed python interpreters for talker and listener
custom_install(talker)
custom_install(listener)
