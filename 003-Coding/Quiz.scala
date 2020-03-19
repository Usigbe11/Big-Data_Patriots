import scala.collection.mutable.ListBuffer
object Quiz {
  def main(args: Array[String]): Unit = {
    var numList: ListBuffer[Int] = ListBuffer()
    for (x <- 0 until 30) {
      numList += scala.util.Random.nextInt()
    }

    def nameAndID(name: String, ID: String): String = {
      return name + ID
    }

    nameAndID("Carl", "123")

    def removeDuplicates(objectList: ListBuffer[String]) =
    {
      var varList : ListBuffer[String] = ListBuffer()
      for (x <- 0 until objectList.length)
      {
        for (j<- 1 until objectList.length)
          {
            if (objectList(j) == objectList(x))
            {
              objectList.patch(j, objectList, 1)
            }
          }
      }
      print(objectList)
    }

    var testList: ListBuffer[String] = ListBuffer("sun","mon","sun")
    removeDuplicates(testList)


    def smallestMissingInteger(numList: List[Int]) =
    {
      if (numList.min < 0)
      {
        var min: Int = numList.min
        while (min < 0)
        {
          min = min + 1
        }
        while (numList.contains(min))
        {
          min = min + 1
        }
        print(min)
      }
      if (numList.min > 0)
      {
        print(numList.min)
      }
    }
    var testNums:List[Int] = List(-2,-3,-1,0,1,2,5,6)
    smallestMissingInteger(testNums)

  }
}

