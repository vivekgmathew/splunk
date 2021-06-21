    package com.panw

    import org.apache.log4j.{Level, Logger}
    import org.apache.spark.sql.SparkSession
    import org.apache.spark.sql.functions._

    object FixingELA extends App {
      val spark = SparkSession.builder().master("local").getOrCreate()
      spark.sparkContext.setLogLevel("ERROR")

      val rootLogger = Logger.getRootLogger()
      rootLogger.setLevel(Level.ERROR)

      Logger.getLogger("org.apache.spark").setLevel(Level.WARN)
      Logger.getLogger("org.spark-project").setLevel(Level.WARN)

      import spark.implicits._
      val ss = Seq(
        ("12", "TP", "l1a", "l2b", "l3c", 2, 1),
        ("13", "TP", "l1a", "l2b", "l3c", 2, 1),
        ("12", "TP", "l1a", "l2b", "l3c", 2, 1),
        ("11", "TP", "l1a", "l2b", "l3c", 2, 1)
      ).toDF(Seq("acc_id", "prod_type", "level_one", "level_two", "level_three", "dep_qty", "cons_qty"): _*)
        .withColumn("sold_qty", lit("0").cast("double"))
        .withColumn("is_from_sold", lit("0").cast("double"))
        .groupBy("acc_id", "prod_type", "level_one", "level_two", "level_three")
        .agg(
          sum("dep_qty") as "dep_qty",
          sum("cons_qty") as "cons_qty",
          sum("sold_qty") as "sold_qty",
          sum("is_from_sold") as "is_from_sold"
        )


      val bkg = Seq(
        ("12", "TP", "l1a", "l2b", "l3c", 2),
        ("13", "TP", "l1a", "l2b", "l3c", 2),
        ("12", "TP", "l1a", "l2b", "l3c", 2)
      ).toDF(Seq("acc_id", "prod_type", "level_one", "level_two", "level_three", "sold_qty"): _*)
        .withColumn("dep_qty", lit("0").cast("double"))
        .withColumn("cons_qty", lit("0").cast("double"))
        .withColumn("is_from_sold", lit("1.0").cast("double"))
        .select("acc_id", "prod_type", "level_one", "level_two", "level_three", "dep_qty", "cons_qty",
        "sold_qty", "is_from_sold")
        .groupBy("acc_id", "prod_type", "level_one", "level_two", "level_three")
        .agg(
          sum("dep_qty") as "dep_qty",
          sum("cons_qty") as "cons_qty",
          sum("sold_qty") as "sold_qty",
          sum("is_from_sold") as "is_from_sold"
        )


      bkg.show(false)

      val unionDf = ss.union(bkg)
      unionDf.show(false)

      val agg = unionDf.groupBy("acc_id", "prod_type", "level_one", "level_two", "level_three")
        .agg(
          sum("dep_qty") as "dep_qty",
          sum("cons_qty") as "cons_qty",
          sum("sold_qty") as "sold_qty",
          sum("is_from_sold") as "is_from_sold"
        )

      agg.show(false)
    }
