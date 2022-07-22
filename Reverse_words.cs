

using System.Collections.Generic;
using System.Linq;
using System;

public class Kata
{
  public static string SpinWords(string sentence)
  { 
    string x = "";
    string[] words = sentence.Split(' ');
    foreach (var item in words){
      if (item.Length >= 5){
        char[] revArray = item.ToCharArray();
        Array.Reverse(revArray);
        x += String.Join("",revArray) + " ";
      }
      else {
              x += item + " "; 
      }
    }
    return x.Trim();
  }
}
