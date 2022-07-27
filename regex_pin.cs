// codewars challenge: ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
//If the function is passed a valid PIN string, return true, else return false.
//Examples (Input --> Output)
//"1234"   -->  true
//"12345"  -->  false
//"a234"   -->  false

using System;
using System.Text.RegularExpressions;

public class Kata
{
  public static bool ValidatePin(string pin)
  {
    bool valid = false;
    if((Regex.IsMatch(pin, @"^\d+$") && pin.Length == 4) || (Regex.IsMatch(pin, @"^\d+$") && pin.Length == 6))
    {
      valid = true;
    }
    return valid;
  }
}

//failed one test gotta figure this one out
//ValidatePin should return false in various edge cases
//Test Failed
//  Wrong output for "123
//"
//  Expected: False
//  But was:  True
