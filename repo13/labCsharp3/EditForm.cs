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
    public partial class EditForm : Form
    {
        private bool isChanged;
        private Phone _phone;

        public Phone Phone
        {
            get { return _phone; }
            set { _phone = value; }
        }
        public EditForm()
        {
            InitializeComponent();

            _phone = new Phone();
        }
        public EditForm(Phone phone)
        {
            InitializeComponent();

            _phone = new Phone(phone);

            textBox_name.Text = _phone.Name;
            textBox_art.Text = _phone.Art;
            textBox_price.Text = _phone.Price;
            textBox_date.Text = _phone.Date;

            isChanged = false;
        }

        private void btn_save_Click(object sender, EventArgs e)
        {
            saveChanges();
        }

        private void btn_no_Click(object sender, EventArgs e)
        {
            if (isChanged)
            {
                DialogOK_Cancel dialog = new DialogOK_Cancel("Save changes?");
                DialogResult result = dialog.ShowDialog();
                if (result == DialogResult.OK)
                {
                    DialogResult = DialogResult.OK;
                    saveChanges();
                }
            }
        }

        private void textBox_art_TextChanged(object sender, EventArgs e)
        {
            isChanged = true;
        }
        private void textBox_price_TextChanged(object sender, EventArgs e)
        {
            isChanged = true;
        }
        private void textBox_date_TextChanged(object sender, EventArgs e)
        {
            isChanged = true;
        }
        private void textBox_name_TextChanged(object sender, EventArgs e)
        {
            isChanged = true;
        }
        private void saveChanges()
        {

            _phone.Name = textBox_name.Text;
            _phone.Art = textBox_art.Text;
            _phone.Price = textBox_price.Text;
            _phone.Date = textBox_date.Text;

        }
       private void textBox_Validating(object sender, CancelEventArgs e)
        {
            TextBox textBox = sender as TextBox;
            e.Cancel = String.IsNullOrEmpty(textBox.Text);
            errorProvider1.SetError(textBox, "Field connot be empty");

        }

        
    }
}
