var str = "", x,y,a;

for (a = 1; a <= 100; a++) 
{
    if (a % 3 == 0 & a % 5 == 0)
    {
        result = "fizzbuzz";
    } else {
        if (a % 3 == 0)
        {
            result = "fizz";
        } else
        {
            if (a % 5 == 0) 
                {
                    result = "buzz";
                }
            else {result = a;}
        }
    }

    console.log(result);
}
