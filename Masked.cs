// Codewars Challenge: ur task is to write a function maskify, which changes all but the last four characters into '#'.
// Examples
// "4556364607935616" --> "############5616"

using System;

public static class Kata
{
  public static string Maskify(string cc)
  {
    int x = cc.Length - 4;
    int y = 0;
    string masked = "";

    foreach(var i in cc)
    {
      if(y < x)
      {
        masked += "#";
        y++;
      }
      else
      {
        masked += i;
      }
    }
    return masked;
  }
}
