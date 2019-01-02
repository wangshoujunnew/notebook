from pyspark import SparkContext,SparkConf
from pyspark.sql import HiveContext

conf = SparkConf()
conf.setAppName('sjw_pyspark')
conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
conf.set("hive.metastore.uris", "thrift://hadoop16:9083") # 设置hive元数据
conf.set("hive.metastore.warehouse.dir","hdfs://nameservice1/home/data/hive/warehouse")  # 设置hive数据仓库位置
sc = SparkContext(conf = conf)
hive_context = HiveContext(sc)
hive_context.sql('use warehouse')
hive_context.sql('select order_no from warehouse.mar_order limit 10').show()
