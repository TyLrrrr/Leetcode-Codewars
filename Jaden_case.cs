// Codewars Challenge: Your task is to convert strings to how they would be written by Jaden Smith. 
// The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
// Example:
// Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
// Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

using System;
public static class JadenCase
{
  public static string ToJadenCase(this string phrase)
  {
    string jaden = "";
    var x = 0;
    string[] toUpper = phrase.Split(' ');
    foreach(var i in toUpper)
    {
      var y = toUpper[x];
      toUpper[x] = char.ToUpper(y[0]) + y.Substring(1);
      x++;
    }
    jaden = string.Join(" ", toUpper);
    Console.WriteLine(jaden);
    return jaden.Trim();
  }
}
