# Databricks notebook source
integer_values = [10, 20, 20, 30, 40, 10, 40, 20, 20, 20, 20, 50]
df = spark.createDataFrame([(value,) for value in integer_values], ["id"])

# COMMAND ----------

integer_values = [30, 20 , 40, 50]
df2 = spark.createDataFrame([(value,) for value in integer_values], ["id2"])

# COMMAND ----------

import pyspark.sql.functions as F
joined_df = df.join(F.broadcast(df2), df.id == df2.id2, 'inner')
joined_df.show()

# COMMAND ----------

#executed_plan = joined_df._jdf.queryExecution().executedPlan()
#print(executed_plan.toString())
#joined_df.explain()

# COMMAND ----------

spark.conf.set("spark.sql.join.preferSortMergeJoin", "false")
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", 2)
print(spark.conf.get("spark.sql.join.preferSortMergeJoin"))

# COMMAND ----------

joined_df = df.join(df2.hint("SHUFFLE_HASH"), df.id == df2.id2, 'inner')
joined_df.display()

# COMMAND ----------

joined_df.explain()

# COMMAND ----------

# MAGIC %md
# MAGIC ### SHUFFLE SORT MERGE JOIN

# COMMAND ----------

spark.conf.set("spark.sql.join.preferSortMergeJoin", "true")
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", -1)
print(spark.conf.get("spark.sql.join.preferSortMergeJoin"))

joined_df = df.join(df2.hint("MERGE"), df.id == df2.id2)
joined_df.display()

# COMMAND ----------

joined_df.explain()

# COMMAND ----------

# MAGIC %md
# MAGIC ### BROADCAST NESTED LOOP JOIN

# COMMAND ----------

import pyspark.sql.functions as F
spark.conf.set("spark.sql.join.preferSortMergeJoin", "true")
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "10485760b")
print(spark.conf.get("spark.sql.join.preferSortMergeJoin"))


joined_df = df.join(F.broadcast(df2), df.id >= df2.id2, 'inner')
joined_df.display()

# COMMAND ----------

joined_df.explain()

# COMMAND ----------

# MAGIC %md
# MAGIC ###  Cartesian Product Join

# COMMAND ----------

import pyspark.sql.functions as F

joined_df = df.join(df2.hint("SHUFLEE_REPLICATE_NL"), df.id >= df2.id2, 'inner')
joined_df.display()

# COMMAND ----------

joined_df.explain()

# COMMAND ----------

