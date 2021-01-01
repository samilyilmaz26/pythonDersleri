using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace yarış
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        Random rnd = new Random();

        private void btnBaşla_Click_1(object sender, EventArgs e)
        {
            BaslayaGel();
            tmBasla.Enabled = true;
        }
        private void tmBasla_Tick(object sender, EventArgs e)
        {

            pcBoxBeyazAt.Left += rnd.Next(1, 10);
            pcBoxSiyahAt.Left += rnd.Next(1, 10);
            if (pcBoxBeyazAt.Right > panel1.Left || pcBoxSiyahAt.Right >= panel1.Left)
            {
                tmBasla.Enabled = false;
                if (pcBoxSiyahAt.Right > pcBoxBeyazAt.Right)
                {
                    MessageBox.Show("Siyah at kazandı");
                }
                else if (pcBoxSiyahAt.Right < pcBoxBeyazAt.Right)
                {
                    MessageBox.Show("Beyaz at kazandı");

                }
                else MessageBox.Show("Berabere Kaldınız");

            }
        }

        private void btnBaslangıc_Click(object sender, EventArgs e)
        {
            BaslayaGel();
        }
        private void BaslayaGel()
        {
            pcBoxBeyazAt.Left = 0;
            pcBoxSiyahAt.Left = 0;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            int interval = tmBasla.Interval;
            int zorluk = Convert.ToInt32(cmBoxZorluk.SelectedItem) * interval;
            tmBasla.Interval = zorluk;
            //int interval = tmBasla.Interval * Convert.ToInt32(cmBoxZorluk.SelectedItem);

        }

        private void btnGeri_Click(object sender, EventArgs e)
        {
            pcBoxBeyazAt.Left += rnd.Next(-10,-1) ;
            pcBoxSiyahAt.Left += rnd.Next(-10, -1);
            if (pcBoxBeyazAt.Right > panel1.Left || pcBoxSiyahAt.Right >= panel1.Left)
            {
                tmBasla.Enabled = false;
                if (pcBoxSiyahAt.Right > pcBoxBeyazAt.Right)
                {
                    MessageBox.Show("Siyah at kazandı");
                }
                else if (pcBoxSiyahAt.Left < pcBoxBeyazAt.Left)
                {
                    MessageBox.Show("Beyaz at kazandı");

                }
                else MessageBox.Show("Berabere Kaldınız");
            }
        }
       
    }
}



//int a çevirmek zorundayız seçilen kutudaki yazılanlar her sey olabilir int string gibi obje olarak koyar bu sebeple adını