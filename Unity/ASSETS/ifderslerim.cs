using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ifderslerim: MonoBehaviour
{

    /*
     < küçükse
     > büyükse
     >= büyük eþit
     <= küçük eþit
     == eþitse
     != eþit deðilse
    */
    int sayi1 = 5, sayi2 = 10, sayi3 = 3;
    void Start()
    {
        if (sayi1 > sayi2)
        {
            Debug.Log("1.Koþul");
        }

        else if (sayi1 > sayi3)
        {
            Debug.Log("2.Koþul");
        }

        else
        {
            Debug.Log("3.Koþul");
        }






        /*
        if (kosul)
        {

            //bu kosul saðlanýrsa burasý çalýþcak
        }

        else if (kosul2)
        {


        }

        else
        {
            // koþul saðlanmazsa

        }
        */

    }


    
}
