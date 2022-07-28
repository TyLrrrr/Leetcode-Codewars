// Codewars Challenge: build a tower 

using System;

public class Kata
{
  public static string[] TowerBuilder(int nFloors)
  { 
    if (nFloors == 1)
    {
      return new []{ "*" };
    }
       
    var result = new string[nFloors];
    for (int row =0; row < nFloors; row++)
    {
        var level = "";
        var midpoint = ((2 * nFloors - 1) / 2);

        for (int col =0; col < 2 * nFloors - 1; col++)
        {
            if((midpoint-row <= col) && (midpoint + row >= col))
            {
                level += "*";
            }
            else
            {
                level += " ";
            } 
        }
        result[row] = string.Concat(new string(level.ToString()));
    }
    return result; 
  }
}
