namespace yarış
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.pcBoxBeyazAt = new System.Windows.Forms.PictureBox();
            this.pcBoxSiyahAt = new System.Windows.Forms.PictureBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.btnBaşla = new System.Windows.Forms.Button();
            this.tmBasla = new System.Windows.Forms.Timer(this.components);
            this.btnBaslangıc = new System.Windows.Forms.Button();
            this.cmBoxZorluk = new System.Windows.Forms.ComboBox();
            this.label1 = new System.Windows.Forms.Label();
            this.btnGeri = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pcBoxBeyazAt)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pcBoxSiyahAt)).BeginInit();
            this.SuspendLayout();
            // 
            // pcBoxBeyazAt
            // 
            this.pcBoxBeyazAt.Image = global::yarış.Properties.Resources.SİYAH_beyaz_;
            this.pcBoxBeyazAt.Location = new System.Drawing.Point(0, 333);
            this.pcBoxBeyazAt.Name = "pcBoxBeyazAt";
            this.pcBoxBeyazAt.Size = new System.Drawing.Size(259, 194);
            this.pcBoxBeyazAt.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pcBoxBeyazAt.TabIndex = 1;
            this.pcBoxBeyazAt.TabStop = false;
            // 
            // pcBoxSiyahAt
            // 
            this.pcBoxSiyahAt.Image = global::yarış.Properties.Resources.BEYAZ;
            this.pcBoxSiyahAt.Location = new System.Drawing.Point(0, 102);
            this.pcBoxSiyahAt.Name = "pcBoxSiyahAt";
            this.pcBoxSiyahAt.Size = new System.Drawing.Size(259, 194);
            this.pcBoxSiyahAt.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pcBoxSiyahAt.TabIndex = 0;
            this.pcBoxSiyahAt.TabStop = false;
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.DarkRed;
            this.panel1.Location = new System.Drawing.Point(1516, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(157, 709);
            this.panel1.TabIndex = 2;
            // 
            // btnBaşla
            // 
            this.btnBaşla.Location = new System.Drawing.Point(-1, 555);
            this.btnBaşla.Name = "btnBaşla";
            this.btnBaşla.Size = new System.Drawing.Size(260, 42);
            this.btnBaşla.TabIndex = 3;
            this.btnBaşla.Text = "Başla";
            this.btnBaşla.UseVisualStyleBackColor = true;
            this.btnBaşla.Click += new System.EventHandler(this.btnBaşla_Click_1);
            // 
            // tmBasla
            // 
            this.tmBasla.Tick += new System.EventHandler(this.tmBasla_Tick);
            // 
            // btnBaslangıc
            // 
            this.btnBaslangıc.Location = new System.Drawing.Point(0, 627);
            this.btnBaslangıc.Name = "btnBaslangıc";
            this.btnBaslangıc.Size = new System.Drawing.Size(260, 42);
            this.btnBaslangıc.TabIndex = 4;
            this.btnBaslangıc.Text = "Başlangıç çizgisine gel";
            this.btnBaslangıc.UseVisualStyleBackColor = true;
            this.btnBaslangıc.Click += new System.EventHandler(this.btnBaslangıc_Click);
            // 
            // cmBoxZorluk
            // 
            this.cmBoxZorluk.FormattingEnabled = true;
            this.cmBoxZorluk.Items.AddRange(new object[] {
            "1",
            "2",
            "3",
            "4",
            "5"});
            this.cmBoxZorluk.Location = new System.Drawing.Point(167, 684);
            this.cmBoxZorluk.Name = "cmBoxZorluk";
            this.cmBoxZorluk.Size = new System.Drawing.Size(121, 33);
            this.cmBoxZorluk.TabIndex = 5;
            this.cmBoxZorluk.Text = "seçiniz";
            this.cmBoxZorluk.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(-6, 684);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(147, 25);
            this.label1.TabIndex = 6;
            this.label1.Text = "Zorluk Derece";
            // 
            // btnGeri
            // 
            this.btnGeri.Location = new System.Drawing.Point(-1, 591);
            this.btnGeri.Name = "btnGeri";
            this.btnGeri.Size = new System.Drawing.Size(260, 42);
            this.btnGeri.TabIndex = 7;
            this.btnGeri.Text = "Geriye Yarış";
            this.btnGeri.UseVisualStyleBackColor = true;
            this.btnGeri.Click += new System.EventHandler(this.btnGeri_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(12F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(1714, 806);
            this.Controls.Add(this.btnGeri);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.cmBoxZorluk);
            this.Controls.Add(this.btnBaslangıc);
            this.Controls.Add(this.pcBoxSiyahAt);
            this.Controls.Add(this.btnBaşla);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.pcBoxBeyazAt);
            this.Name = "Form1";
            this.Text = "Başla Çizgisine Gel";
            ((System.ComponentModel.ISupportInitialize)(this.pcBoxBeyazAt)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pcBoxSiyahAt)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pcBoxSiyahAt;
        private System.Windows.Forms.PictureBox pcBoxBeyazAt;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button btnBaşla;
        private System.Windows.Forms.Timer tmBasla;
        private System.Windows.Forms.Button btnBaslangıc;
        private System.Windows.Forms.ComboBox cmBoxZorluk;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnGeri;
    }
}

