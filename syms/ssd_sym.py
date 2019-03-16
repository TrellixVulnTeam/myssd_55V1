import mxnet as mx
from mxnet import sym, mod, nd

"""
class MySSD(nn.Block):
    def __init__(self, num_cls, num_ach, **kwargs):
        super(MySSD, self).__init__(**kwargs)
        self.num_classes = num_cls
        self.BaseBlk = BaseNetwork(True)
        self.blk1 = nn.Sequential()
        self.blk1.add(nn.Conv2D(channels=1024, kernel_size=3, strides=1, padding=0),
                      nn.Conv2D(channels=1024, kernel_size=1, strides=1, padding=1),
                      nn.BatchNorm(in_channels=1024),
                      nn.Activation('relu'),
                      nn.MaxPool2D(2))

        self.cls1 = genClsPredictor(num_cls, num_ach)
        self.reg1 = genBBoxRegressor(num_ach)

        self.blk2 = nn.Sequential()
        self.blk2.add(nn.Conv2D(channels=256, kernel_size=1, strides=1, padding=0),
                      nn.Conv2D(channels=512, kernel_size=3, strides=1, padding=1),
                      nn.BatchNorm(in_channels=512),
                      nn.Activation('relu'),
                      nn.MaxPool2D(2))

        self.cls2 = genClsPredictor(num_cls, num_ach)
        self.reg2 = genBBoxRegressor(num_ach)

        self.blk3 = nn.Sequential()
        self.blk3.add(nn.Conv2D(channels=128, kernel_size=1, strides=1, padding=0),
                      nn.Conv2D(channels=256, kernel_size=3, strides=1, padding=1),
                      nn.BatchNorm(in_channels=256),
                      nn.Activation('relu'),
                      nn.MaxPool2D(2))

        self.cls3 = genClsPredictor(num_cls, num_ach)
        self.reg3 = genBBoxRegressor(num_ach)

        self.blk4 = nn.Sequential()
        self.blk4.add(nn.Conv2D(channels=128, kernel_size=1, strides=1, padding=0),
                      nn.Conv2D(channels=256, kernel_size=3, strides=1, padding=1),
                      nn.BatchNorm(in_channels=256),
                      nn.Activation('relu'),
                      nn.MaxPool2D(2))

        self.cls4 = genClsPredictor(num_cls, num_ach)
        self.reg4 = genBBoxRegressor(num_ach)

        self.blk5 = nn.Sequential()
        self.blk3.add(nn.Conv2D(channels=128, kernel_size=1, strides=1, padding=0),
                      nn.Conv2D(channels=256, kernel_size=3, strides=1, padding=1),
                      nn.BatchNorm(in_channels=256),
                      nn.Activation('relu'),
                      nn.MaxPool2D(2))

        self.cls5 = genClsPredictor(num_cls, num_ach)
        self.reg5 = genBBoxRegressor(num_ach)

    def forward(self, x):
        x = self.BaseBlk(x)

        anchors, cls_preds, bbox_preds = [None] * 5, [None] * 5, [None] * 5
        for k in range(5):
            if k == 0:
                im = x
            (x, anchors[k], cls_preds[k], bbox_preds[k]) = \
                blk_forward(x, getattr(self, "blk%d" % (k + 1)), sizes[k], ratios[k],
                            getattr(self, "cls%d" % (k + 1)), getattr(self, "reg%d" % (k + 1)))
            # print("layer[%d], fmap shape %s, anchor %s" % (k + 1, x.shape, anchors[k].shape))
        return (im, nd.concat(*anchors, dim=1),
                concat_preds(cls_preds).reshape((0, -1, self.num_classes + 1)),
                concat_preds(bbox_preds))

"""


def getConvLayer(data):
    """
    return a conv layer with act, batchnorm, and pooling layers, if any
    :return:
    """
    convunit = sym.Convolution(data=data)
    convunit = sym.BatchNorm()
    convunit = sym.Activation()
    convunit = sym.Pooling()
    pass


def getBaseNet():
    net = sym.Variable('data')

    pass


def getSSD():
    """
    This is for generation of ssd network symbols
    :return:
    """
    net = sym.Variable('data')
    net = sym.Convolution(data=net, num_filter=128)
    pass


def getPredBranch():
    net = sym.Convolution()
    pass
