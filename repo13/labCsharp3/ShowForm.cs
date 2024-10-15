using Phone_lab2;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace labCsharp3
{
    public partial class ShowForm : Form
    {
        public ShowForm()
        {
            InitializeComponent();
        }
        public ShowForm(Phone phone)
        {
            InitializeComponent();

            textBox_name.Text= phone.Name;
            textBox_art.Text= phone.Art;
            textBox_price.Text= phone.Price;
            textBox_date.Text= phone.Date;
        }

        private void ShowForm_Load(object sender, EventArgs e)
        {

        }
    }
}
