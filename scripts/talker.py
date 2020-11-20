#!/usr/bin/env python
#encoding: utf-8
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$
# Japanese and English comments added

import rospy
from std_msgs.msg import String

def talker():
    # パブリッシャに必要な設定を施す
    # トピック名をchatter、データ型をStringに設定し、メッセージを溜め込む量を10としている
    # Sets the needed configuration for a Publisher
    # The topic name is set to chatter, data type to String, and the buff size to 10
    pub = rospy.Publisher('chatter', String, queue_size=10)
    # talkerという名前でノードを初期化する
    # Initiates this node as the name talker
    rospy.init_node('talker')
    # このノードの周期を10 Hzで設定する
    # Loops this node at 10 Hz
    rate = rospy.Rate(10)
    # ROSが立ち上がっている限り、while文の中が実行される
    # As long as ROS is running
    while not rospy.is_shutdown():
        # hello_str変数にhello worldという文字列と今の時間(日時ではない)を代入する
        # Inserts hello world and the current time in hello_str
        hello_str = "hello world %s" % rospy.get_time()
        # hello_strに代入したものを表示
        # Displays the word string hello_str
        rospy.loginfo(hello_str)
        # hello_strをパブリッシュする
        # Publish the word string hello_str
        pub.publish(hello_str)
        # 周期が10 Hzとなるように調整する
        # Adjusting to match 10 Hz
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
