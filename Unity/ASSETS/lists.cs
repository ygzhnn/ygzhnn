using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class lists : MonoBehaviour
{
    // array list , performans olarak arraylist kötüdür list kullanmamýz gerekiyor.
    // list
    void Start()
    {
        List<int> yaslar = new List<int>();

        yaslar.Add(50);
        yaslar.Add(40);
        yaslar.Add(18);

        List<string> adlar = new List<string>();

        adlar.Add("Yaðýz");
        adlar.Add("Yiðit");
        adlar.Add("Ahmet");
        adlar.Add("Musa");



        //Debug.Log(yaslar.Count);
        //Debug.Log(yaslar[1]);

        /*foreach (var item in yaslar)
        {
            Debug.Log(item);
        }

        for (int i = 0; i < yaslar.Count; i++)
        {
            Debug.Log(yaslar[i]);
        }*/

        yaslar.Insert(1, 90);

        for (int i = 0; i < yaslar.Count; i++)
        {
            Debug.Log(yaslar[i]);
        }

        yaslar.Remove(18);

        for (int i = 0; i < yaslar.Count; i++)
        {
            Debug.Log(yaslar[i]);
        }

        if (adlar.Contains("Yaðýz"))
        {
            Debug.Log("Evet Var");
        }
        else
            Debug.Log("Hayýr Yok");

        yaslar.Clear();


        if (yaslar.Count <= 0)
            Debug.Log("Bu liste temizlenmiþ");


        



    }
}
