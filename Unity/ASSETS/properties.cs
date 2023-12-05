using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class properties : MonoBehaviour
{
    public int altin;
    public int elmas;
    public int Altin
    {
        get
        {
            if (altin <= 50)
                return altin;
            else
                return 0;
        }

        set 
        {
            elmas = 2;
            altin = value;
        }
    }
    int degerEkle(int deger)
    {
        return 3 * deger;
    }

    void Start()
    {
        /* elmas = 2;
         * 
         * Altin = 20;
        Debug.Log(Altin);*/
        Altin = 10 + degerEkle(3);
        Debug.Log(Altin);

      

    }

}
