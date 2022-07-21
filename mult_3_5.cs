using System;

public static class Kata
{
  public static int Solution(int value)
  {
    int x = 0;
    for (int i = 0; i < value; i++)
    {
      if (i % 5 == 0 && i % 3 == 0)
      {
        x += i;
      }
      else if (i % 3 == 0)
      {
        x += i;
      }
      else if (i % 5 == 0)
      {
        x += i;
      }
    }
    return x;
  }
}
