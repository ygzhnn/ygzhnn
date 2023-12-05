using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class propertypatterns : MonoBehaviour
{
    string mulkTipi;
    string blokTipi;
    int benimKatSayim = 2;
    void Start()
    {

        //double aidatCarpanKatSayisi = 2;

        /*double aidatHesapla(propertypatterns classimbenim, int aidatCarpanKatSayisi)
            => classimbenim switch
            {

                { mulkTipi : "Daire"} => aidatCarpanKatSayisi * 1.5,
                { mulkTipi : "Villa" } => aidatCarpanKatSayisi * 2.5,
                { mulkTipi : "Rezidans" } => aidatCarpanKatSayisi * 3.5,
                _=> 0

            };

        mulkTipi = "Rezidans";

        Debug.Log(aidatHesapla(this,2));*/

        double aidatHesapla(propertypatterns classimbenim, int aidatCarpanKatSayisi)
            => classimbenim switch
            {

                { mulkTipi: "Daire", blokTipi: "A"} => aidatCarpanKatSayisi * 1.5,
                { mulkTipi: "Villa", blokTipi: "B" } => aidatCarpanKatSayisi * 2.5,
                { mulkTipi: "Rezidans", blokTipi: "C" } => aidatCarpanKatSayisi * 3.5,
                _ => 0

            };

        mulkTipi = "Daire";
        blokTipi = "A";

        Debug.Log(aidatHesapla(this, benimKatSayim));


    }

    
   
}
