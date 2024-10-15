
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Xml.Linq;

namespace Phone_lab2
{
    public abstract class Shop
    {
        public abstract void Sendproduct();
    }
    public class Phone : Shop
    {
        public string Name { get; set; }
        public string Art { get; set; }
        public string Price { get; set; }
        public string Date { get; set; }

        private int[] arr = new int[] { 51, 2354, 6789, 2534, 7865 };
        
        public int this[int index]
        {
            get { return arr[index]; }
            set { arr[index] = value; }
        }
        private List<string> _phone;
        public List<string> Phones
        {
            get
            {
                return _phone;
            }
            set
            {
                _phone = value;
            }
        }
        public Phone(string name, string art, string price, string date)
        {
            this.Name = name;
            this.Art = art;
            this.Price = price;
            this.Date = date;
        }
        public Phone()
        {
            this.Name = "";
            this.Art = "";
            this.Price = "";
            this.Date = "";
        }
        public Phone(Phone other)
        {
            this.Name = other.Name;
            this.Art = other.Art;
            this.Price = other.Price;
            this.Date = other.Date;

        }
        public virtual void Print()
        {
            Console.WriteLine("Название товара : " + Name);
            Console.WriteLine("Артикул товара : " + Art);
            Console.WriteLine("Цена товара : " + Price);
            Console.WriteLine("Дата создания товара : " + Date);
            Console.WriteLine("");
        }
        public override void Sendproduct()
        {
           /* if (this._status == false)
            {
                this._status = true;
                Console.WriteLine("Товар с артикулом : " + Art + " Отправлент");
                Console.WriteLine("");
            }
            else
            {
                Console.WriteLine("Товар с артикулом : " + Art + " Уже в пути");
                Console.WriteLine("");
            }*/
        }

    }
}