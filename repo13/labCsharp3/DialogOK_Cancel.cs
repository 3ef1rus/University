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
    public partial class DialogOK_Cancel : Form
    {
        public DialogOK_Cancel()
        {
            InitializeComponent();
        }
        public DialogOK_Cancel(string labelText)
        {
            InitializeComponent();
            label1.Text = labelText;
        }

        private void button1_Click(object sender, EventArgs e)
        {
           
        }

        private void DialogOK_Cancel_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }
    }
}
