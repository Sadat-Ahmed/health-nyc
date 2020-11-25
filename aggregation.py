
from pyspark.sql import *
from pyspark.sql.functions import col

spark = SparkSession \
    .builder \
    .appName("CovidStuff") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

covid_df = spark.read.csv("data/COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv",header=True, inferSchema = True )
ed_visit_df = spark.read.csv("data/Emergency_Department_Visits_and_Admissions_for_Influenza-like_Illness_and_or_Pneumonia.csv",header=True, inferSchema = True )


covid_df.show()
ed_visit_df.show()

joined_df = ed_visit_df.join(covid_df, covid_df.DATE_OF_INTEREST == ed_visit_df.date)

joined_df.show()
print("COUNT covid_df {}".format(covid_df.count()))
print("COUNT ed_visit_df {}".format( ed_visit_df.count()))
print("COUNT joined_df {}".format(joined_df.count()))


joined_df.where('DATE_OF_INTEREST' == date).show()

