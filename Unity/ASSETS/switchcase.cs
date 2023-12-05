using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class switchcase : MonoBehaviour
{
    
    void Start()
    {

        string araba = "Bmw";
        

        switch (araba)
        {
            case "Audi":
                Debug.Log("Evet Deger Audi");
                break;
            case "Bmw":
                Debug.Log("Evet Deger Bmw");
                break;
            case "Honda":
                Debug.Log("Evet Deger Honda");
                break;

            default:
                Debug.Log("Uyuþan Kayýt Yok");
                break;
        }

    }

   
}
