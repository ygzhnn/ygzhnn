using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class foreacha : MonoBehaviour
{
    
    void Start()
    {

        string[] urunler = { "elma", "armut", "karpuz" };

        foreach (string str in urunler) 
        {
            Debug.Log(str);
        }
    }

    
}
