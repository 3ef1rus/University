using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Phone_lab2;

namespace labCsharp3
{
    public partial class Phones : Form
    {
        private int currentSelectedIndex = -1;

        BindingList<Phone> phoneList;

        
        public Phones()
        {
            InitializeComponent();
            phoneList = new BindingList<Phone>();
            AddData();
            listBox1.DataSource = phoneList;
            listBox1.DisplayMember = "Name";
        }
        private void AddData()
        {
            phoneList.Add(new Phone("domashni", "7475", "4321", "10.10.2022"));
            phoneList.Add(new Phone("mobil", "1233", "2233", "10.10.2011"));
            phoneList.Add(new Phone("smart", "3211", "5511", "10.10.2033"));
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            currentSelectedIndex = listBox1.SelectedIndex;
        }
       
        private void toolStripButton2_Click(object sender, EventArgs e)
        {
            deleteItemFromList();
        }

        private void toolStripButton3_Click(object sender, EventArgs e)
        {
            editItemInList();
        }

        private void toolStripButton1_Click(object sender, EventArgs e)
        {
            addItemToList();
        }

        private void toolStripButton4_Click(object sender, EventArgs e)
        {
            showItem();
        }
        private void addItemToList()
        {
            Phone emptyObject = new Phone();
            Phone pic = invokeEditForm(emptyObject);
            if (pic == emptyObject)
            {
                return;
            }

            phoneList.Add(pic);
        }
        
        private void editItemInList()
        {
            if (currentSelectedIndex < 0)
            {
                return;
            }

            Phone oldObject = new Phone(phoneList[currentSelectedIndex]);
            Phone pic = invokeEditForm(oldObject);
            if (pic == oldObject)
            {
                return;
            }

            phoneList[currentSelectedIndex] = pic;
        }
        private void deleteItemFromList()
        {
            if (currentSelectedIndex < 0)
            {
                return;
            }

            phoneList.RemoveAt(currentSelectedIndex);
        }

        private void showItem()
        {
            if (currentSelectedIndex < 0)
            {
                return;
            }

            ShowForm show = new ShowForm(phoneList[currentSelectedIndex]);
            show.Show();
        }
        private Phone invokeEditForm(Phone currentPhone)
        {
            EditForm phoneEditForm = new EditForm(currentPhone);
            DialogResult res = phoneEditForm.ShowDialog();
            if (res == DialogResult.OK)
            {
                return phoneEditForm.Phone;
            }

            return currentPhone;
        }
        private void Phone_Load(object sender, EventArgs e)
        {

        }

        private void addToolStripMenuItem_Click(object sender, EventArgs e)
        {
            addItemToList();
        }

        private void deleteToolStripMenuItem_Click(object sender, EventArgs e)
        {
            deleteItemFromList();
        }

        private void editToolStripMenuItem_Click(object sender, EventArgs e)
        {
            editItemInList();
        }

        private void viewToolStripMenuItem_Click(object sender, EventArgs e)
        {
            showItem();
        }

       
    }
}
