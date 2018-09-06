#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import zipfile
from io import BytesIO

from PIL import Image, ImageOps

_mask_cache = {

}


def cut_file(gray_file: bytes, template: str, file: bytes, out="out"):
# def cut_file(gray_file, template, file, out="out"):
    file_by_name = {

    }
    source = Image.open(BytesIO(file))
    source = source.convert("RGBA")
    gray = Image.open(BytesIO(gray_file))

    def min_pic(img):
        mask = img.split()[-1]
        box = mask.getbbox()
        return img.crop(box)

    def get_piece(source, mask_list):
        piece = []
        for each in mask_list:
            canvas = Image.new("RGBA", (source.width, source.height), (255, 255, 255, 0))
            canvas.paste(source, mask=each)
            piece.append(canvas)
        return piece

    def _mask_template(template, w, h):
        if _mask_cache.get(template) is None:
            orig = Image.open("mask/%s_0.png" % template).split()
            grid, mask0 = orig[0], orig[-1]
            tpl = {
                "grid": grid,
                "mask0": mask0,
                "mask": [],
                "size": 0
            }
            tpl["w"] = grid.width
            tpl["h"] = grid.height
            for f in sorted(list(filter(lambda x: x.startswith("%s_" % template), os.listdir("mask/")))):
                filename, _, ext = f.rpartition(".")
                if filename.endswith("_0") or not filename.startswith("%s_" % template):
                    continue
                mask = Image.open("mask/%s" % f).split()[0]
                mask = ImageOps.invert(mask)
                canvas = Image.new('L', (tpl["w"], tpl["h"]), 0)
                canvas.paste(mask, mask=mask0)
                tpl["mask"].append(canvas)
            tpl["size"] = len(tpl["mask"])
            _mask_cache[template] = tpl
        tpl = _mask_cache[template]
        if tpl["w"] != w or tpl["h"] != h:
            _ = {
                "grid": tpl["grid"].resize((w, h)),
                "mask0": tpl["mask0"].resize((w, h)),
                "mask": list(map(lambda x: x.resize((w, h)), tpl["mask"])),
                "size": tpl["size"],
            }
            return _
        return tpl

    tpl = _mask_template(template, source.width, source.height)
    gray_piece = get_piece(gray.resize(source.size), tpl["mask"])
    piece = get_piece(source, tpl["mask"])

    def merge_img_list(img_list):
        canvas = Image.new("RGBA", img_list[0].size, (255, 255, 255, 0))
        for each in img_list:
            canvas.paste(each, mask=each.split()[-1])
        return canvas

    # noinspection PyShadowingNames
    def draw(mask_ids):
        return merge_img_list(list(map(lambda i_x: (gray_piece if str(i_x[1]) == "0" else piece)[i_x[0]], enumerate(mask_ids))))

    output = BytesIO()
    img_list = []

    def get_img_bytes(img):
        tmp = BytesIO()
        img.save(tmp, format="png")
        tmp.flush()
        return tmp.getbuffer()

    with zipfile.ZipFile(output, mode="w", compression=zipfile.ZIP_STORED, allowZip64=False) as doc:
        # 碎片预览图
        for n in range(2 ** tpl["size"]):
            seq = list(reversed(("0" * tpl["size"] + bin(n)[2:])[-tpl["size"]:]))
            content = get_img_bytes(draw(seq))
            img_file_name = "%s.png" % "_".join(seq)
            img_list.append(img_file_name)
            file_by_name["%s" % img_file_name] = content
            doc.writestr(img_file_name, content)
        # 碎片图
        for seq, each in enumerate(piece):
            content = get_img_bytes(min_pic(each))
            img_file_name = "%s.png" % (seq + 1)
            img_list.append(img_file_name)
            file_by_name["%s" % img_file_name] = content
            doc.writestr(img_file_name, content)

    if not os.path.exists(out):
        os.mkdir(out)
    for filename, content in file_by_name.items():
        with open(os.path.join(out, filename), mode="bw") as fout:
            fout.write(content)


if __name__ == '__main__':
    def _read_file(file) -> bytes:
    # def _read_file(file):
        with open(file, mode="rb") as fin:
            return fin.read()


    assert os.path.exists("0.png"), "0.png不存在"
    assert os.path.exists("1.png"), "1.png不存在"
    for _ in range(1, 7):
        assert os.path.exists("mask/6_%s.png" % _), "mask文件[6_%s]不存在" % _
    cut_file(_read_file("0.png"), "6", _read_file("1.png"))
