"""
Resource Py
    Updates the resource rc files in the code blocks project.
        fv = FileVersion
        cn = CompanyName
        fd = FileDescription
        in = InternalName
        lc = LegalCopyright
        lt = LegalTrademark
        pn = ProductName
        pv = ProductVersion
"""
import sys
import os
import argparse
from jinja2 import Template
from pathlib import Path

def addArgs():
    parser = argparse.ArgumentParser()
    helpmsg = "String for FileVersion"
    parser.add_argument("-fv", "--FileVersion", help=helpmsg)
    helpmsg = "String for CompanyName"
    parser.add_argument("-cn", "--CompanyName", help=helpmsg)
    helpmsg = "String for FileDescription"
    parser.add_argument("-fd", "--FileDescription", help=helpmsg)
    helpmsg = "String for InternalName"
    parser.add_argument("-in", "--InternalName", help=helpmsg)
    helpmsg = "String for LegalCopyright"
    parser.add_argument("-lc", "--LegalCopyright", help=helpmsg)
    helpmsg = "String for LegalTrademark"
    parser.add_argument("-lt", "--LegalTrademark", help=helpmsg)
    helpmsg = "String for ProductName"
    parser.add_argument("-pn", "--ProductName", help=helpmsg)
    helpmsg = "String for ProductVersion"
    parser.add_argument("-pv", "--ProductVersion", help=helpmsg)
    helpmsg = "String for Original File Name"
    parser.add_argument("-ofn", "--OriginalFileName", help=helpmsg)
    helpmsg = "Input complete file path for template"
    parser.add_argument("-i", "--InputTemplate", help=helpmsg)
    helpmsg = "Output file name and path for rc file"
    parser.add_argument("-i", "--OutputFileNameWithPath", help=helpmsg)
    return parser

def getTemplate(templatefilepath):
    f = open(templatefilepath, mode='r')
    template_text = f.read()
    f.close()
    return template_text

def writeTemplate(outputfilenamewithpath,template_text):
    f = open(outputfilenamewithpath, mode='w')
    f.write(template_text)
    f.close()

def main():
    args = sys.argv[1:]
    parser = addArgs()
    args = parser.parse_args(args)
    # Set template variables
    data = {}
    print(args)
    # Template Data
    data["productname_t"]       = args.ProductName
    data["productversion_t"]    = args.ProductVersion
    data["legaltrademark_t"]    = args.LegalTrademark
    data["legalcopyright_t"]    = args.LegalCopyright
    data["internalname_t"]      = args.InternalName
    data["filedescription_t"]   = args.FileDescription
    data["companyname_t"]       = args.CompanyName
    data["fileversion_t"]       = args.FileVersion
    data["originalfilename_t"]  = args.OriginalFileName
    # Template file Path
    templatefilepath            = args.InputTemplate
    outputfilenamewithpath      = args.OutputFileNameWithPath
    # Set Default if none
    if data["productname_t"] == None:
        data["productname_t"] = "EOS"
    if data["productversion_t"] == None:
        data["productversion_t"] = "0.0.0.0"
    if data["legaltrademark_t"] == None:
        data["legaltrademark_t"] = "Bombardier Transportation India Pvt Ltd."
    if data["legalcopyright_t"] == None:
        data["legalcopyright_t"] = "Bombardier Transportation"
    if data["internalname_t"] == None:
        data["internalname_t"] = ""
    if data["filedescription_t"] == None:
        data["filedescription_t"] = "Developed using code blocks commit x"
    if data["companyname_t"] == None:
        data["companyname_t"] = "Bombardier Transportation"
    if data["fileversion_t"] == None:
        data["fileversion_t"] = "0.0.0.0"
    if data["originalfilename_t"] == None:
        data["originalfilename_t"] = ""
    # To be added value checks
    # But currently the inputs are provided by a different automated system with 
    # these exact parameters hence not adding now.
    # Check for python 3
    p = Path(templatefilepath)
    if p.exists():
        template_text = getTemplate(p)
        j2_template = Template(template_text)
        writeTemplate(outputfilenamewithpath,j2_template.render(data))
    else:
        sys.stdout.write("Input Template file doesnt exists at path - ")
        sys.stdout.write(templatefilepath)
        return 1 
    

if __name__ == "__main__":
    main()