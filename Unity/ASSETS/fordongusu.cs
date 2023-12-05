using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class fordongusu : MonoBehaviour
{
    int disaridansayim = 3;
    void Start()
    {
        for (int sayi = 0; sayi < disaridansayim; sayi++)
        {
            if (sayi == 2) break;
            Debug.Log("Sayýnýn Deðeri = " + sayi);
        }
    }

}
