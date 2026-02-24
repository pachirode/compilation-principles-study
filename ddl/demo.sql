CREATE TABLE `order_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `orderNo` varchar(50) NOT NULL COMMENT '订单编号',
  `userId` int(11) NOT NULL COMMENT '用户ID',
  `totalAmount` decimal(12,2) NOT NULL COMMENT '订单总金额',
  `status` tinyint(2) NOT NULL DEFAULT 0 COMMENT '订单状态 0-待支付 1-已支付 2-已发货 3-已完成 4-已取消',
  `isInvoice` bit(1) DEFAULT b'0' COMMENT '是否开发票 0-否 1-是',
  `invoiceTitle` varchar(100) DEFAULT NULL COMMENT '发票抬头',
  `remark` text COMMENT '订单备注',
  `receiverAddress` varchar(255) NOT NULL COMMENT '收货地址',
  `payTime` datetime DEFAULT NULL COMMENT '支付时间',
  PRIMARY KEY (`id`),
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8 COMMENT='订单信息表';