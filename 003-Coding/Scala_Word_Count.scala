import scala.io.Source
import scala.collection.mutable.ListBuffer
object Counter {

  def main(args: Array[String]): Unit =
  {
    val myFile: Source = Source.fromFile("/home/fieldemployee/Downloads/Example.txt")
    var linelist: ListBuffer[String] = ListBuffer()
    var count: ListBuffer[Integer] = ListBuffer()
    var word: ListBuffer[String] = ListBuffer()
    var i: Int = 0
    for (line <- myFile.getLines()) {
      linelist += line
    }
    var officiallist: List[String] = linelist.toList
    for (x <- 0 to officiallist.length -1)
      {
        var nextWordList:Array[String] = linelist(x).split(" ")
        for (y <- 0 to nextWordList.length -1)
          {
            var nextWord:String = nextWordList(y)
            if (word.contains(nextWord))
            {
              var index:Int = word.indexOf(nextWord)
              count(index) = count(index) + 1

            }
            else
            {
              word += nextWord
              count += 1
            }
          }
      }

    for (j <- 0 to count.length - 1)
      {
        print (word(j) +" : "+ count(j) + " ")
      }
    myFile.close()
  }
}
