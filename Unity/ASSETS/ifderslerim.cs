using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ifderslerim: MonoBehaviour
{

    /*
     < k���kse
     > b�y�kse
     >= b�y�k e�it
     <= k���k e�it
     == e�itse
     != e�it de�ilse
    */
    int sayi1 = 5, sayi2 = 10, sayi3 = 3;
    void Start()
    {
        if (sayi1 > sayi2)
        {
            Debug.Log("1.Ko�ul");
        }

        else if (sayi1 > sayi3)
        {
            Debug.Log("2.Ko�ul");
        }

        else
        {
            Debug.Log("3.Ko�ul");
        }






        /*
        if (kosul)
        {

            //bu kosul sa�lan�rsa buras� �al��cak
        }

        else if (kosul2)
        {


        }

        else
        {
            // ko�ul sa�lanmazsa

        }
        */

    }


    
}
