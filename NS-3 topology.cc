source tb_compat.tcl
 set ns [new Simulator]
 
 # Create the center node (named by its variable name)
 set nodeAtt [$ns node]
 set nodeA [$ns node]
 set nodeB [$ns node]
 set nodeC [$ns node]
 set nodeD [$ns node]
 set nodeServ [$ns node]

 tb-set-node-os $nodeA WINXP-UPDATE
 tb-set-node-os $nodeB Ubuntu1404-64-STD
 tb-set-node-os $nodeC Ubuntu1404-64-STD
 tb-set-node-os $nodeD Ubuntu1404-64-STD
 tb-set-node-os $nodeAtt WINXP-UPDATE
 tb-set-node-os $nodeServ Ubuntu1404-64-STD

 set link0 [$ns duplex-link $nodeAtt $nodeA 100Mb 10ms DropTail]
  tb-set-link-loss $link0 0.01
  set link1 [$ns duplex-link $nodeAtt $nodeB 100Mb 10ms DropTail]
  tb-set-link-loss $link1 0.01
  set link2 [$ns duplex-link $nodeAtt $nodeC 100Mb 10ms DropTail]
  tb-set-link-loss $link2 0.01
  set link3 [$ns duplex-link $nodeAtt $nodeD 100Mb 10ms DropTail]
  tb-set-link-loss $link3 0.01

  set link4 [$ns duplex-link $nodeA $nodeServ 100Mb 10ms DropTail]
  tb-set-link-loss $link4 0.01
  set link5 [$ns duplex-link $nodeB $nodeServ 100Mb 10ms DropTail]
  tb-set-link-loss $link5 0.01
  set link6 [$ns duplex-link $nodeC $nodeServ 100Mb 10ms DropTail]
  tb-set-link-loss $link6 0.01
  set link7 [$ns duplex-link $nodeD $nodeServ 100Mb 10ms DropTail]
  tb-set-link-loss $link7 0.01

   # Creation boilerplate
   $ns rtptoto Static
   $ns run