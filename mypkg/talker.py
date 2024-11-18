import rclpy                                        #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node                         #ノードを実装するためのNodeクラス
from std_msgs.msg import Int16                      #通信の型（16ビットの符号付き整数）

rclpy.init()
node = Node("talker")                               #ノードを作成（nodeというオブジェクトを作成）
pub = node.create_publisher(Int16, "countup", 10)   #pubというパブリッシャのオブジェクトを作成
n = 0                                               #カウント用変数

def cb():                                           #17行目で定期的に実行されるコールバック関数
    global n                                        #関数を抜けてもnがリセットされないようglobal変数にしている
    msg = Int16()                                   #メッセージの「オブジェクト」
    msg.data = n                                    #msgオブジェクトの持つdataにnを結びつけ
    pub.publish(msg)                                #pubの持つpublishでメッセージ送信
    n += 1                                          #nの値が1増加

def main():                                         #main関数
    node.create_timer(0.5, cb)                      #nodeオブジェクトのタイマの設定（0.5秒ごとにcb関数を実行）
    rclpy.spin(node)                                #nodeオブジェクトを実行(無限ループ)
    
